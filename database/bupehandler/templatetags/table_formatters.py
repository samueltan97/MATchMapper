from django import template
from django.utils.safestring import mark_safe
import phonenumbers
from datetime import datetime

register = template.Library()


@register.simple_tag(name="date_last_updated", takes_context=True)
def bu_options(context):
    date_time_str = context["objects"][0]["date_update"]
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    formattedDate = date_time_obj.strftime("%B %-d, %Y")

    return mark_safe(formattedDate)

@register.filter("legal_url", is_safe=True)
def phone_number(illegal):
    if illegal is None:
        return ""
    splitIllegal = illegal.split(":")
    if splitIllegal[0] == "https://" or splitIllegal[0] == "http://":
        return mark_safe(illegal)
    else:
        return "//" + illegal

@register.filter("notArchiveOnly", is_safe=True)
def phone_number(objs):
    goodObjs = []
    return objs

@register.filter("format_phone", is_safe=True)
def phone_number(s):
    if s is None or s == "":
        return ""
    parsed = phonenumbers.parse(s, "US")
    autoFormatted = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
    rawNoExt = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
    ext = ""
    splitNumber = autoFormatted.split(" ")
    if len(splitNumber) == 4:
        ext = "x" + splitNumber[3]
    linkText = " "
    linkText = linkText.join(splitNumber[0:2])

    html = f'<a target="_blank" href="tel:{rawNoExt}">{linkText}</a> {ext}'

    return mark_safe(html)

@register.simple_tag(name="bu_options", takes_context=True)
def bu_options(context):
    site = context["site"]
    options = []
    if site["bwn"]:
        options.append("With naloxone (ex. Suboxone)")
    if site["bwon"]:
        options.append("Without naloxone")
    if site["beri"]:
        options.append("Injectable extended-release (ex. Sublocade)")
    if site["bsdm"]:
        options.append("Sub-dermal implant (Probuphine)")
    options = ";<br/>".join(options) + ";"
    if options == "":
        print("options is empty")
    return mark_safe(options)

@register.simple_tag(name="nu_options", takes_context=True)
def nu_options(context):
    site = context["site"]
    options = []
    if site["vtrl"]:
        options.append("Vivitrol (injectable)")
    if site["nxn"]:
        options.append("Oral naltrexone")
    options = ";<br/>".join(options) + ";"
    return mark_safe(options)

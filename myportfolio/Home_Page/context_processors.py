from Home_Page.models import FooterSettings, FooterLink, FooterContact, FooterSocialLink


def footer_data(request):
    settings_obj = FooterSettings.objects.first()
    quick_links = FooterLink.objects.filter(section='quick', is_active=True)
    course_links = FooterLink.objects.filter(section='course', is_active=True)
    contacts = FooterContact.objects.filter(is_active=True)
    socials = FooterSocialLink.objects.filter(is_active=True)

    return {
        'footer_settings': settings_obj,
        'footer_quick_links': quick_links,
        'footer_course_links': course_links,
        'footer_contacts': contacts,
        'footer_social_links': socials,
    }

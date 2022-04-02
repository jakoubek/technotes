def define_env(env):
    "Definition of the module"

    @env.macro
    def feedback(title, section, slug):
        email_address = f"{section}+{slug}@technotes.jakoubek.net"
        md = "\n\n## Feedback / Kontakt\n\n"
        md += f"Wenn Sie Fragen oder Anregungen zum Artikel *{title}* haben, senden Sie mir bitte eine E-Mail an: [{email_address}](mailto:{email_address}?subject=[Technotes] {title})"
        return md


# def on_post_page_macros(env):
    # env.raw_markdown += "{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}"
#     env.raw_markdown += '\n\n## Feedback / Kontakt\n\n'
#     env.raw_markdown += 'Wenn Sie Fragen oder Anregungen zum Artikel *' + \
#         env.page.title + '* haben ...'
#     env.raw_markdown += env.page.abs_url

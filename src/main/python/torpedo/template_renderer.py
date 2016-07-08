from jinja2 import Template


class TemplateRenderer(object):
    @staticmethod
    def render_template(self, template_path: str, dest_path: str, config: dict):
        with open(template_path, "r") as template:
            with open(dest_path, "w") as destination:
                destination.write(str(Template(template, trim_blocks=True).render(config)).strip())

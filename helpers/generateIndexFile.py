from string import Template
def generateHtml(images):
    html = Template("""<!DOCTYPE html><html><style></style><body><img src="$img1"></body></html>""")
    html = html.substitute({'img1': images[0]})
    return html
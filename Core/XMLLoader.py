import xml.etree.ElementTree as ET
from Core.Body import Body
from Core.NPC import NPC


def get_text(parent, tag, default=""):
    element = parent.find(tag)
    if element is None or element.text is None:
        return default
    return element.text.strip()


def load_npc_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    body_node = root.find("Body")

    body = Body(
        race=get_text(body_node, "Race") if body_node is not None else "",
        species=get_text(root, "Species"),
        variant=get_text(root, "Variant"),
        sex=get_text(root, "Sex")
    )

    npc = NPC(
        name=get_text(root, "Name"),
        age=get_text(root, "AgeDisplay", get_text(root, "Age")),
        body=body,
        behavior=get_text(root.find("Behavior"), "CurrentState") if root.find("Behavior") is not None else "",
        backstory=get_text(root, "Backstory")
    )

    return npc

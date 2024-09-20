# split xml files

from xml.dom.minidom import parse
import codecs
import os
import xml.etree.ElementTree as ET

def split_xml(xml_file,out_path):
    
    dom_tree = parse(xml_file)
    collection = dom_tree.documentElement
    for idx, si in enumerate(collection.getElementsByTagName("si")):
        sid = si.getAttribute('id')

        # out_xml_path = os.path.join(out_path,sid)
        # with codecs.open(out_xml_path, "w", encoding="utf-16") as out_xml:
        print(sid)
            # dom_tree.writexml(out_xml, encoding="utf-16")

def read_xml(xml_file):
    tree = ET.parse(xml_file)
    collection = tree.documentElement
    # xml_string = "<root><element>Value</element></root>"
    # root = ET.fromstring(xml_string
    # print(root)
    root = tree.getroot()
    for elem in root:
        # print(elem.tag,elem.attrib,elem.text)
        # print(elem.get())
        print(enumerate(collection.getElementsByTagName(elem)))

    # sid = root.find("0010001")
    # print(sid)


if __name__ == "__main__":
    read_xml(r"D:\users\v-zhazhai\Tools\Tools\code\zh-CN_TTS\test.xml")

import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LTImage, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

from Translate import translate

import fire


def parse(file_name, target_name):
    fp = open(file_name, 'rb')
    praser = PDFParser(fp)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)

    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        page_number = 1
        for page in doc.get_pages():
            print('page: ' + str(page_number))
            interpreter.process_page(page)
            layout = device.get_result()
            # 这里layout是一个LTPage对象，里面存放着这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            # 想要获取文本就获得对象的text属性
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(target_name, 'a') as f:
                        results = x.get_text()
                        translate_text = translate(results)
                        f.write(translate_text + '\n')
                # if (isinstance(x, LTImage)):
                #     with open('patternColoring.txt', 'a') as f:
                #         results = x.get_image()
                #         f.write('###########\n' + results + '\n')
            page_number += 1


if __name__ == '__main__':
    fire.Fire(parse)

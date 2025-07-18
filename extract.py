import re

def parse_invoice_data(text):
    data = {}
    data['num_facture'] = re.search(r"(Facture\s*№|رقم الفاتورة)\s*[:\-]?\s*(\w+)", text)
    data['date'] = re.search(r"(Date|التاريخ)\s*[:\-]?\s*(\d{2}/\d{2}/\d{4})", text)
    data['montant_ttc'] = re.search(r"(TTC|المجموع)\s*[:\-]?\s*([\d\s,.]+)", text)

    # Nettoyage
    for k, v in data.items():
        data[k] = v.group(2).strip() if v else None

    return data

import pymupdf


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extract text from a PDF resume.

    Args:
        file_bytes: PDF file as bytes

    Returns:
        Extracted text from all pages
    """

    document = pymupdf.open(
        stream=file_bytes,
        filetype="pdf"
    )

    text = []

    for page in document:
        page_text = page.get_text("text")

        if page_text:
            text.append(page_text)

    document.close()

    return "\n".join(text).strip()
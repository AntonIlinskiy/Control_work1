
with open("2.txt", "r", encoding="utf-8") as file:
    content = file.read()
    modified_content = content.replace("дождь", "ДОЖДЬ")


with open("2_raint.txt", "w", encoding="utf-8") as file:
    file.write(modified_content)
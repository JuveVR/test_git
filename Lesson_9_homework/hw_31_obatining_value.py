

# Get value of href attribute for tag a. Do it:
#
# using string methods
# using regular expressions
# Expected result for attached wiki_page.txt file is:
#     ['111/wiki/HTML111', '222/wiki/Form_(HTML)222', '333NEW333', '444/wiki/Image_map#Server-side444',
#      '555/w/index.php?title=Query_string&amp;action=edit&amp;section=2555', '666/wiki/Form_(HTML)666']


# with regexp
import re


def hrefs_values_regex(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    pattern = re.compile(r'<a [^>]*href="([^"]+)"')
    hrefs = pattern.findall(content)

    return hrefs


file_path = 'wiki_page.txt'
hrefs_values = hrefs_values_regex(file_path)
print(hrefs_values)


# with strings methods
def hrefs_values_str(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    hrefs = []
    position = 0

    while True:
        start_position = content.find("<a ", position)
        if start_position == -1:
            break

        end_position = content.find(">", start_position)
        if end_position == -1:
            break

        tag = content[start_position:end_position + 1]

        href_start = tag.find('href="')
        if href_start != -1:
            href_start += len('href="')
            href_end = tag.find('"', href_start)
            href = tag[href_start:href_end]
            hrefs.append(href)
        position = end_position + 1
    return hrefs


file_path = 'wiki_page.txt'
hrefs_str = hrefs_values_str(file_path)
print(hrefs_str)




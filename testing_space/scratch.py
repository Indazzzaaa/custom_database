import csv

import random

# Set up the CSV file
filename = 'data.csv'
fieldnames = ['id', 'name', 'age', 'city', 'salary']

# Generate and write the data to the CSV file
with open(file=filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1, 100001):
        writer.writerow({
            'id': i,
            'name': f'User {i}',
            'age': random.randint(20, 60),
            'city': f'City {random.randint(1, 10)}',
            'salary': random.randint(5000, 50000)
        })


def csv_to_html( file_name,csv_file=filename,rows_per_page=10):
    # Read CSV file
    with open(csv_file, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        data = [row for row in csvreader]

    # Paginate data
    pages = []
    page = []
    for i, row in enumerate(data):
        if i > 0 and i % rows_per_page == 0:
            pages.append(page)
            page = []
        page.append(row)
    pages.append(page)

    # Create HTML table with pagination
    html = '<table>\n<thead>\n<tr>'
    for h in header:
        html += f'<th>{h}</th>'
    html += '</tr>\n</thead>\n<tbody>\n'
    for i, page in enumerate(pages):
        html += f'<div class="page" id="page-{i+1}">'
        html += '<table class="table">\n<thead>\n<tr>'
        for h in header:
            html += f'<th>{h}</th>'
        html += '</tr>\n</thead>\n<tbody>\n'
        for row in page:
            html += '<tr>\n'
            for value in row:
                html += f'<td>{value}</td>\n'
            html += '</tr>\n'
        html += '</tbody>\n</table>\n</div>\n'
    html += '</tbody>\n</table>\n'

    # Add pagination links
    html += '<div class="pagination">\n'
    for i in range(len(pages)):
        html += f'<a href="#page-{i+1}">{i+1}</a>\n'
    html += '</div>\n'

    # Add CSS styles
    css = '<style>\n'
    css += 'table {\nborder-collapse: collapse;\n}\n'
    css += 'th, td {\nborder: 1px solid black;\npadding: 5px;\n}\n'
    css += 'tr:nth-child(even) {\nbackground-color: #f2f2f2;\n}\n'
    css += '.pagination {\nmargin-top: 10px;\n}\n'
    css += '.pagination a {\ndisplay: inline-block;\nmargin-right: 5px;\n}\n'
    css += '</style>\n'

    # Combine HTML and CSS
    html = f'<html>\n<head>\n{css}</head>\n<body>\n{html}</body>\n</html>'

    # Write the HTML file
    with open(file_name, 'w') as f:
        f.write(html)



csv_to_html(file_name='data.html',rows_per_page=10)

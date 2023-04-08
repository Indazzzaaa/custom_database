import csv

def read_data(file_path, page_size, page_num):
    start_index = (page_num - 1) * page_size + 1
    end_index = start_index + page_size
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)
        header = data[0]
        rows = data[start_index:end_index]

    return header, rows

def generate_table(header, rows):
    table_html = '<table>\n'
    # Generate table header
    table_html += '<thead>\n<tr>\n'
    for col in header:
        table_html += f'<th>{col}</th>\n'
    table_html += '</tr>\n</thead>\n'
    
    # Generate table body
    table_html += '<tbody>\n'
    for row in rows:
        table_html += '<tr>\n'
        for val in row:
            table_html += f'<td>{val}</td>\n'
        table_html += '</tr>\n'
    table_html += '</tbody>\n</table>\n'
    
    return table_html

def generate_pagination(file_path, page_size, current_page):
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)
        num_rows = len(data) - 1
        num_pages = num_rows // page_size + 1
    
    pagination_html = '<div class="pagination">\n'
    for i in range(1, num_pages+1):
        if i == current_page:
            pagination_html += f'<a class="active" href="#">{i}</a>\n'
        else:
            pagination_html += f'<a href="?page={i}">{i}</a>\n'
    pagination_html += '</div>\n'
    
    return pagination_html

def generate_html(file_path, page_size, current_page):
    header, rows = read_data(file_path, page_size, current_page)
    table_html = generate_table(header, rows)
    pagination_html = generate_pagination(file_path, page_size, current_page)
    
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSV Table</title>
        <style>
            table {{
              font-family: Arial, sans-serif;
              border-collapse: collapse;
              width: 100%;
            }}
            
            th, td {{
              border: 1px solid #dddddd;
              text-align: left;
              padding: 8px;
            }}
            
            tr:nth-child(even) {{
              background-color: #dddddd;
            }}
            
            .pagination {{
              display: flex;
              justify-content: center;
            }}
            
            .pagination a {{
              color: black;
              float: left;
              padding: 8px 16px;
              text-decoration: none;
              border: 1px solid #ddd;
            }}
            
            .pagination a.active {{
              background-color: #4CAF50;
              color: white;
              border: 1px solid #4CAF50;
            }}
            
            .pagination a:hover:not(.active) {{
              background-color: #ddd;
            }}
        </style>
    </head>
    <body>
        <h1>CSV Table</h1>
        {table_html}
        {pagination_html}
    </body>
    </html>
    '''
    
    return html


# create a CSV file with 10000 rows and 5 columns
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'])
    for i in range(1, 10001):
        writer.writerow(['Row ' + str(i) + ' Column 1', 'Row ' + str(i) + ' Column 2',
                         'Row ' + str(i) + ' Column 3', 'Row ' + str(i) + ' Column 4',
                         'Row ' + str(i) + ' Column 5'])

# read the CSV file and generate pagination HTML
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    pagination_html = generate_pagination_html(rows, 10)

# write the pagination HTML to a file
with open('pagination.html', 'w') as htmlfile:
    htmlfile.write(pagination_html)
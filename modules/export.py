# Data export module

def export_csv(separator, *serie):
    """Save data as CSV"""
    file = open("temp/output.csv", "w")
    size=len(serie)
    longest=0
    count=1
    for data in serie:
        file.write(f'{data.get_X_label()}{separator}{data.get_Y_label()}')
        if(count!=size):
            file.write(separator)
            count+=1
        if(len(data)>longest): longest=len(data)
    file.write("\n")
    for i in range(longest):
        count=1
        for data in serie:
            if(data[i]!=None):
                file.write(f'{data[i].x}{separator}{data[i].y}')
            if(count!=size):
                file.write(separator)
                count+=1
        file.write("\n")


def export_xlsx(data, filename):
    """Save data as XLSX"""

    pass

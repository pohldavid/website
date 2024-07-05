

# csv file of the form weight, date, time
#read and write out as markdown table


def make_weight_table(file = 'thgiew.txt'):

    with open('weight.md', 'w') as table:
        table.write("| Weight | Date   | Time  | \n")
        table.write("| :---:  | :----: | :---: | \n")
  
        with open(file, 'r') as weight:    

            for line in weight:
                line = line.strip().split(",")  
                row = f"| {line[0]} | {line[1]} | {line[2]} | \n"
                print(row)
                table.write(row)

if __name__ == "__main__":
    make_weight_table()
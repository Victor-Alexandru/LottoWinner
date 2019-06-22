import itertools

if __name__ == '__main__':
    def write_list_to_file(param_list, file_name):
        with open(file_name, "w") as file:
            pString = ""
            index = 1
            for combination in param_list:
                pString += "Combinarea nr " + str(index) + " " + str(combination) + " \n"
                index += 1
            file.write(pString)


    def main():
        init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        six_taken = list(itertools.combinations(init_list, 6))
        five_taken = list(itertools.combinations(init_list, 5))
        four_taken = list(itertools.combinations(init_list, 4))

        write_list_to_file(six_taken, "f1.txt")
        write_list_to_file(five_taken, "f2.txt")
        write_list_to_file(four_taken, "f3.txt")


    main()

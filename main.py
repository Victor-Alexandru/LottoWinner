import itertools

init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    def write_list_to_file(param_list, file_name):
        with open(file_name, "w") as file:
            pString = ""
            index = 1
            for combination in param_list:
                pString += "v" + str(index) + "(" + file_name + ")" + str(combination) + " \n"
                index += 1
            file.write(pString)


    def get_sets(set_length, init_length):
        init_sets = []
        aux = set()

        for i in range(1, init_length + 1):
            if len(aux) == set_length:
                init_sets.append(aux.copy())
                aux.clear()
            aux.add(i)

        if len(aux) == set_length:
            init_sets.append(aux)
        if len(aux) < set_length:
            for i in range(1, init_length + 1):
                aux.add(i)
                if (len(aux) == set_length):
                    break
        init_sets.append(aux.copy())
        return init_sets


    def get_cover_sets(set_one, set_two, set_length):
        set_list = [set_one, set_two]

        difference = set_one.difference(set_two).union(set_two.difference(set_one))
        while len(difference) > set_length:
            aux = set()
            for i in range(0, set_length):
                aux.add(difference.pop())
            set_list.append(aux)

        while len(difference) != set_length:
            for item in init_list:
                if item not in difference and len(difference) != set_length:
                    difference.add(item)

        set_list.append(difference)

        return set_list


    def main():

        six_taken = list(itertools.combinations(init_list, 6))
        five_taken = list(itertools.combinations(init_list, 5))
        four_taken = list(itertools.combinations(init_list, 4))

        A, B = get_sets(6, 10)[0], get_sets(6, 10)[1];

        result = get_cover_sets(A, B, 6)

        print(result)


    main()

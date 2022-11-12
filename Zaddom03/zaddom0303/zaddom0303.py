# Maciej Cieszyński

def counter_generator(start=0):
    digits = 2
    petitioner_number = start
    while True:
        if petitioner_number < 100:
            yield str(petitioner_number).zfill(digits)
            petitioner_number = petitioner_number + 1
        else:
            petitioner_number = 0

if __name__ == '__main__':
    tickets = counter_generator(22)
    for ticket in tickets:
        print(ticket)

        input('NACIŚNIJ ENTER')
        # UWAGA! Nieskończona pętla!
    pass

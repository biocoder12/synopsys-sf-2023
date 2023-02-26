#
#
#
ml_viruses_list_file_name = "ml_viruses.list"
taxanomy_list_file_name = "taxanomy_semi_colons_list.txt"

def file_to_list(file_name):
    my_file = open(file_name, "r")  
    data = my_file.read()
    return data.split("\n")

# printing the data
ml_virus_list = file_to_list(ml_viruses_list_file_name)
print("ML Viruses = ", len(ml_virus_list))
tax_virus_list = file_to_list(taxanomy_list_file_name)
print("TAX Viruses = ", len(tax_virus_list))

final_virus = []
not_found_virus = []

genome_found = False
for ml_virus in ml_virus_list:
    # print("Checking: ", ml_virus)
    genome_found = False
    for tax_virus in tax_virus_list:
        # tokens = tax_virus.split(";")[::-1]
        if ml_virus in tax_virus:
            genome_found = True
            final_virus.append(tax_virus)
            break
    if not genome_found:
        not_found_virus.append(ml_virus)

# for tax_virus in tax_virus_list:
#     if tax_virus.split(":")[0] == "Homo sapiens":
#         final_virus.append(tax_virus)

final_virus_set = set(final_virus)
not_found_virus_set = set(not_found_virus)

print(len(final_virus))
print(len(final_virus_set))
# print("\n".join(final_virus))

print("------------------- NOT FOUND ------------")
print(len(not_found_virus))
print(len(not_found_virus_set))
print("\n".join(not_found_virus_set))

print("------------------- MISSING ------------")
for nf_virus in not_found_virus_set:
    for tax_virus in tax_virus_list:
        tokens = tax_virus.split(";")[::-1]
        if (tokens[0] in nf_virus):
            print("Missing: ", nf_virus, tax_virus)
            break
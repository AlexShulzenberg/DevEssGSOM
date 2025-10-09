text = "Before departure, all students leaving for exchange studies should fill in a specializedapplication form. An application should be submitted in 1 copy and not later than 2 weeks priorto departure for the exchange semester, provided that the students do not have any academicfailure. The paper should be submitted to the International Academic Mobility Office(Volkhovsky per., 3, office 207, Tel.: +7 (812) 323 8447). A copy of the invitation letter from ahost school - partner of GSOM SPbU has to be attached to the application."


address_string_start = text.find("(") + 1

add_string_end = text.find(", Tel")

the_address = text[address_string_start:add_string_end]

print(the_address)
types = {
    1: "Блокирующий",
    2: "Критический",
    3: "Значительный",
    4: "Незначительный",
    5: "Тривиальный",
}

tickets = {
    1: ["API_45", "API_76", "E2E_4"],
    2: ["UI_19", "API_65", "API_76", "E2E_45"],
    3: ["E2E_45", "API_45", "E2E_2"],
    4: ["E2E_9", "API_76"],
    5: ["E2E_2", "API_61"],
}


def remove_duplicates(tickets_dict):
    seen = set()
    result = {}

    for severity in sorted(tickets_dict.keys()):
        unique_tickets = []
        for ticket in tickets_dict[severity]:
            if ticket not in seen:
                unique_tickets.append(ticket)
                seen.add(ticket)
        result[severity] = unique_tickets
    return result


def assign_ticket_types(types_dict, tickets_dict):
    clean_tickets = remove_duplicates(tickets_dict)
    result = {}

    for key in sorted(types_dict.keys()):
        result[types_dict[key]] = clean_tickets.get(key, [])

    return result


tickets_by_type = assign_ticket_types(types, tickets)

print(tickets_by_type)

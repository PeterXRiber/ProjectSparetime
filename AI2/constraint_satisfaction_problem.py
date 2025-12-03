from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        unassigned_variables = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(unassigned_variables, assignment):
            if self.is_consistent(unassigned_variables, value, assignment):
                assignment[unassigned_variables] = value
                result = self.recursive_backtracking(assignment)
                ## Eventually refactor line 23-25
                if result:
                    return result
                assignment.pop[unassigned_variables]
        return False

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True
        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue
                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_southAmerica_csp():
    costaRica, Panama, Colombia, Ecuador, Venezuela, Guyana, Suriname, GuyanaFr, Peru, Brasil, Bolivia, Paraguay, Chile, Argentina, Uruguay = 'costaRica', 'Panama', 'Colombia', 'Ecuador', 'Venezuela', 'Guyana', 'Suriname', 'GuyanaFr', 'Peru', 'Brasil', 'Bolivia', 'Paraguay', 'Chile', 'Argentina', 'Uruguay'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [costaRica, Panama, Colombia, Ecuador, Venezuela, Guyana, Suriname, GuyanaFr, Peru, Brasil, Bolivia,
                 Paraguay, Chile, Argentina, Uruguay]
    domains = {
        costaRica: values[:],
        Panama: values[:],
        Colombia: values[:],
        Ecuador: values[:],
        Venezuela: values[:],
        Guyana: values[:],
        Suriname: values[:],
        GuyanaFr: values[:],
        Peru: values[:],
        Brasil: values[:],
        Bolivia: values[:],
        Paraguay: values[:],
        Chile: values[:],
        Argentina: values[:],
        Uruguay: values[:],

    }

    neighbours = {
        costaRica: [Panama],
        Panama: [Colombia],
        Colombia: [Ecuador, Venezuela],
        Ecuador: [Colombia, Peru],
        Venezuela: [Colombia, Guyana, Brasil],
        Guyana: [Venezuela, Suriname, Brasil],
        Suriname: [Guyana, GuyanaFr, Brasil],
        GuyanaFr: [Suriname, Brasil],
        Peru: [Colombia, Ecuador, Brasil, Bolivia, Chile],
        Brasil: [GuyanaFr, Suriname, Guyana, Venezuela, Colombia, Peru, Bolivia, Paraguay, Argentina, Uruguay],
        Bolivia: [Brasil, Peru, Chile, Argentina, Paraguay],
        Paraguay: [Brasil, Bolivia, Argentina],
        Chile: [Argentina, Bolivia, Peru],
        Argentina: [Chile, Bolivia, Paraguay, Uruguay],
        Uruguay: [Argentina, Brasil],

    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        costaRica: constraint_function,
        Panama: constraint_function,
        Colombia: constraint_function,
        Ecuador: constraint_function,
        Venezuela: constraint_function,
        Guyana: constraint_function,
        Suriname: constraint_function,
        GuyanaFr: constraint_function,
        Peru: constraint_function,
        Brasil: constraint_function,
        Bolivia: constraint_function,
        Paraguay: constraint_function,
        Chile: constraint_function,
        Argentina: constraint_function,
        Uruguay: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    southAmerica = create_southAmerica_csp()
    result = southAmerica.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html

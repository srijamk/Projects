# Calculates cost of widgets and gizmos.

class WidgetsAndGizmos():
    WIDGET_COST = 75
    GIZMO_COST = 112
    def widget_and_gizmo_cost(self, widgets, gizmos):
        return "Your total cost is $%.2f." \
        % (widgets * self.WIDGET_COST + gizmos * self.GIZMO_COST)

widgets = int(input("Enter the number of widgets here: "))
gizmos = int(input("Enter the nubmer of gizmos here: "))

calculate = WidgetsAndGizmos()
print calculate.widget_and_gizmo_cost(widgets, gizmos)

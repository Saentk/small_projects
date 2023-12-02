# Landscaping Services Program
# Zackery Tookes, CMIS102/7380
# Date

import sys, datetime

# Constants
MOWING_COST = 0.05  # $ per sq ft
EDGING_COST = 0.50  # $ per linear ft
SHRUB_PRUNING_COST = 10.00  # $ per shrub
TAX_RATE_NY_NJ = 0.10
TAX_RATE_OTHER = 0.08

# Services
MOWING = 1
EDGING = 2
SHRUB_PRUNING = 3
ALL = 4

def main():
    display_name_class_date()
    service = display_menu()
    cost = calculate_cost(service)
    tax = calculate_tax(cost)
    display_output(service, cost, tax)

def display_name_class_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print("Name: Zackery Tookes")
    print("Class: CMIS102/7380")
    print("Date:", current_date)

def display_menu():
    print("Services:")
    print(f"{MOWING}. Mowing (${MOWING_COST}/sq ft)")
    print(f"{EDGING}. Edging (${EDGING_COST}/linear ft)")
    print(f"{SHRUB_PRUNING}. Shrub Pruning (${SHRUB_PRUNING_COST}/shrub)")
    print(f"{ALL}. All Services\n")

    service = int(input("Select a service (1-4): "))
    if service not in (MOWING, EDGING, SHRUB_PRUNING, ALL):
        print("Invalid choice. Please enter a number between 1 and 4.")
        sys.exit(1)

    return service

def calculate_cost(service):
    if service == MOWING:
        sq_ft = float(input("Enter the yard's square footage: "))
        cost = sq_ft * MOWING_COST
    elif service == EDGING:
        linear_ft = float(input("Enter the yard's linear footage: "))
        cost = linear_ft * EDGING_COST
    elif service == SHRUB_PRUNING:
        shrubs = int(input("Enter the number of shrubs: "))
        cost = shrubs * SHRUB_PRUNING_COST
    else:
        sq_ft = float(input("Enter the yard's square footage: "))
        linear_ft = float(input("Enter the yard's linear footage: "))
        shrubs = int(input("Enter the number of shrubs: "))
        cost = sq_ft * MOWING_COST + linear_ft * EDGING_COST + shrubs * SHRUB_PRUNING_COST

    return cost

def calculate_tax(cost):
    state = input("Enter the state lived (e.g., NY, NJ, GA): ")
    if state.upper() in ('NY', 'NJ'):
        tax_rate = TAX_RATE_NY_NJ
    else:
        tax_rate = TAX_RATE_OTHER

    return cost * tax_rate

def display_output(service, cost, tax):
    total_cost = cost + tax

    print("\nService Selected:", service)
    print("Cost of Service: $", round(cost, 2))
    print("Tax Amount: $", round(tax, 2))
    print("Final Cost: $", round(total_cost, 2))

if __name__ == "__main__":
    main()

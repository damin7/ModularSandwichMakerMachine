import data
import cashier
import sandwich_maker


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes

sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)

cashier_instance = cashier.Cashier()


def order_sandwich():
    while True:
        print("What size sandwich would you like? (small/medium/large/off/report): ")
        choice = input().lower()

        if choice in ("small", "medium", "large"):
            order_ingredients = recipes[choice]["ingredients"]
            cost = recipes[choice]["cost"]

            if sandwich_maker_instance.check_resources(order_ingredients):
                print(f"The cost for the {choice.capitalize()} sandwich is: ${cost}")

                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, order_ingredients)

            elif choice == "off":
                print("Shutting down the machine")
                break

            elif choice == "report":
                for ingredient, quantity in sandwich_maker_instance.machine_resources.items():
                    unit = "slice(s)" if ingredient != "cheese" else "ounce(s)"
                    print(f'{ingredient.capitalize()}: {quantity} {unit}')

            else:
                print("Invalid input. Please choose from small, medium, large, off, or report.")





def main():
    ###  write the rest of the codes ###
    order_sandwich()



if __name__=="__main__":
    main()

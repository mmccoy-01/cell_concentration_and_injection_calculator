while True:
    # Ask the user for input and store the responses in variables
    live_cell_count = float(input("What is your live cell count (e6) in 1mL? "))
    total_live_cell_count_suspension = float(input("In mL, what is your current suspension? "))
    inj_num = int(input("How many mice are being injected? "))
    inj_desired = float(input("How many cells (e6) do you want to inject per mouse? "))
    
    # Calculate cell_diff
    cell_diff = round((total_live_cell_count_suspension * live_cell_count) - (inj_desired * inj_num), 3)
    
    if (inj_desired * inj_num) <= (total_live_cell_count_suspension * live_cell_count):
        desired_cell_suspension_per_mouse = round((inj_num * inj_desired) / (live_cell_count)**2, 3)
        max_cells_per_mouse = round((total_live_cell_count_suspension * live_cell_count) / inj_num, 3)
        max_cells_suspension_per_mouse = round(max_cells_per_mouse / live_cell_count, 3)
        
        print(f"Congratulations, you have enough cells plus {cell_diff}e6 extra cells.")
        print(f"You can inject {inj_desired}e6 cells per mouse in {desired_cell_suspension_per_mouse}mL.")
        print(f"At most, you can inject {max_cells_per_mouse}e6 cells per mouse in {max_cells_suspension_per_mouse}mL.")
        
        choice_increase_cells = input(f"Given this information, would you like to increase the number of cells from {inj_desired}e6 cells per mouse? (y/n): ")
        
        if choice_increase_cells.lower() == 'y':
            continue  # Restart the loop to ask for the new desired cell count.
        elif choice_increase_cells.lower() == 'n':
            inj_per_epp = float(input("How many injections do you want per eppendorf tube? "))
            num_of_epp = round((live_cell_count * total_live_cell_count_suspension) / (inj_per_epp * inj_desired), 3)
            inj_vol = float(input("What is the injection volume in uL? "))
            epp_vol = (inj_per_epp * inj_vol) / 1000
            pbs_vol = epp_vol - (inj_desired * desired_cell_suspension_per_mouse * inj_per_epp)
            
            print()
            print(f"If you use all of the cells, you'll have a total of {num_of_epp} eppendorf tubes with {inj_per_epp} injections of {inj_desired}e6 cells each.")
            print(f"You'll need exactly {round(inj_num / inj_per_epp, 3)} eppendorf tubes for exactly {inj_num} injections.")
            print(f"A single eppendorf tube should have {inj_per_epp * inj_desired}e6 cells in {round(inj_desired * desired_cell_suspension_per_mouse * inj_per_epp, 3)}mL from cell concentration.")
            print(f"Add {round(pbs_vol, 3)}mL of PBS to get a total eppendorf volume of {round(epp_vol, 3)}mL")
            print()
            
            print("If everything looks good, we're going to proceed with a few more experiment-related questions so that you can get nicely formatted documentation.")
            print()
            
            inj_date = input("What is today's date? ")
            num_inj_vials = input("How many vials were thawed? ")
            name_inj_vials = input("What were the name(s) of the injection vial(s)? If there is more than one name, separate with commas ")
            total_cell_count = float(input("What was the total cell count (e6) in 1mL? "))
            cell_via = float(input("What was the cell viability (%)? "))
            
            print()
            print("Below is the official documentation that you can copy and paste:")
            print()
            
            print(f"On {inj_date}, {num_inj_vials} vials of {name_inj_vials} were thawed with a total cell count of {total_cell_count}e6 cells and a viability of {cell_via}%.")
            print(f"There were {live_cell_count}e6 cells per 1mL and that was suspended in {total_live_cell_count_suspension}mL for a live total cell concentration of {live_cell_count * total_live_cell_count_suspension}e6 cells.")
            print(f"{inj_num} mice were injected with {inj_desired}e6 cells each at {round(inj_vol, 0)}uL.")
            print(f"{inj_desired}e6 cells were in {desired_cell_suspension_per_mouse}mL from the original {total_live_cell_count_suspension}mL suspension.")
            print(f"{round(inj_num / inj_per_epp, 3)} eppendorf tubes were used for exactly {inj_num} injections.")
            print(f"Each eppendorf tube had {inj_per_epp} injections with {inj_desired * desired_cell_suspension_per_mouse * inj_per_epp}mL of {inj_per_epp * inj_desired}e6 cells from the original {total_live_cell_count_suspension}mL cell suspension and {round(pbs_vol, 3)}mL of PBS was added to get a total eppendorf volume of {round(epp_vol, 3)}mL for each eppendorf tube.")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
            break
    else:
        choice = input("Sorry, you do not have enough cells for injections. Can you thaw more cells? (y/n): ")
        if choice.lower() == 'n':
            max_cells_per_mouse = round((total_live_cell_count_suspension * live_cell_count) / inj_num, 3)
            max_cells_suspension_per_mouse = round(max_cells_per_mouse / live_cell_count, 3)
            
            print(f"The maximum allowed number of cells to inject per mouse is {max_cells_per_mouse}e6 cells in {max_cells_suspension_per_mouse}mL.")
            break

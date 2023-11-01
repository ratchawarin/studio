or row in data:
                tree.insert("", "end", values=row)

            number_of_ids = len(tree.get_children())
            total_amount = number_of_ids * 800

            # Display the total amount
            total_label = Label(currentwindow, text=f"Total Amount: {total_amount} Baht", font=("DB HELVETHAICA X BD EXT", 20))
            total_label.grid(row=1, column=0, padx=50, pady=20)
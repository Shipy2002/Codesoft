import tkinter as tk
from tkinter import messagebox

contacts = []


def add_contact():
    name = entry_name.get()
    phone_number = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone_number:
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }

        contacts.append(contact)
        update_contact_list()
        clear_entries()

        messagebox.showinfo("Success", f"Contact {name} added successfully!")
    else:
        messagebox.showerror("Error", "Name and phone number are required!")


def update_contact_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone_number']}")


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


def search_contact():
    query = entry_search.get()
    search_results = []

    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone_number']:
            search_results.append(contact)

    update_search_results(search_results)


def update_search_results(results):
    listbox.delete(0, tk.END)
    for result in results:
        listbox.insert(tk.END, f"{result['name']} - {result['phone_number']}")


def update_contact():
    selected_index = listbox.curselection()

    if selected_index:
        index = selected_index[0]
        contact = contacts[index]

        new_phone_number = entry_new_phone.get()
        new_email = entry_new_email.get()
        new_address = entry_new_address.get()

        if new_phone_number:
            contact['phone_number'] = new_phone_number
        if new_email:
            contact['email'] = new_email
        if new_address:
            contact['address'] = new_address

        update_contact_list()
        clear_update_entries()

        messagebox.showinfo("Success", f"Contact {contact['name']} updated successfully!")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")


def delete_contact():
    selected_index = listbox.curselection()

    if selected_index:
        index = selected_index[0]
        deleted_contact = contacts.pop(index)

        update_contact_list()
        clear_update_entries()

        messagebox.showinfo("Success", f"Contact {deleted_contact['name']} deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")


def clear_update_entries():
    entry_new_phone.delete(0, tk.END)
    entry_new_email.delete(0, tk.END)
    entry_new_address.delete(0, tk.END)


def view_all_contacts():
    update_contact_list()


# Create main window
root = tk.Tk()
root.title("Contact Management System")

# Labels and Entries for adding a contact
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, sticky=tk.W)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0, sticky=tk.W)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, sticky=tk.W)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0, sticky=tk.W)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1)

button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_add.grid(row=4, column=1, pady=10)

# Listbox for displaying contacts
listbox = tk.Listbox(root, width=40, height=10)
listbox.grid(row=0, column=2, rowspan=10, padx=10)

# Labels and Entries for searching contacts
label_search = tk.Label(root, text="Search:")
label_search.grid(row=10, column=0, sticky=tk.W)
entry_search = tk.Entry(root)
entry_search.grid(row=10, column=1)

button_search = tk.Button(root, text="Search", command=search_contact)
button_search.grid(row=10, column=2, pady=10)

# Labels and Entries for updating contacts
label_new_phone = tk.Label(root, text="New Phone:")
label_new_phone.grid(row=11, column=0, sticky=tk.W)
entry_new_phone = tk.Entry(root)
entry_new_phone.grid(row=11, column=1)

label_new_email = tk.Label(root, text="New Email:")
label_new_email.grid(row=12, column=0, sticky=tk.W)
entry_new_email = tk.Entry(root)
entry_new_email.grid(row=12, column=1)

label_new_address = tk.Label(root, text="New Address:")
label_new_address.grid(row=13, column=0, sticky=tk.W)
entry_new_address = tk.Entry(root)
entry_new_address.grid(row=13, column=1)

button_update = tk.Button(root, text="Update Contact", command=update_contact)
button_update.grid(row=14, column=1, pady=10)

# Button for deleting contacts
button_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
button_delete.grid(row=14, column=2, pady=10)

# Button for viewing all contacts
button_view_all = tk.Button(root, text="View All Contacts", command=view_all_contacts)
button_view_all.grid(row=15, column=1, pady=10)

# Start the main loop
root.mainloop()
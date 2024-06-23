import flet as ft

import base64
def main(page: ft.Page):
    page.title = "Routes Example"
    page.window_width = 370
    page.theme_mode = "light"
    ph = ft.PermissionHandler()
    page.overlay.append(ph)

    logo = ft.Image(
        src=f"/logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    def check_permission():
        print("Checking")
        o = ph.check_permission(ft.PermissionType.STORAGE)
        if o != "PermissionStatus.Granted":
           alert("Permission","Oops")
           request_permission()

    def request_permission():
        print("Requesting")
        o = ph.request_permission(ft.PermissionType.STORAGE)
        

    def alert(title,message):
        dlg = ft.AlertDialog(
                title=ft.Text(value=title,size=16),
                content=ft.Text(value=message),
                actions=[
                     ft.TextButton("Okay")
                ],
                
            )
        page.dialog = dlg
        dlg.open = True
        page.update()


    def switch_theme(theme_change):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            theme_change.icon = ft.icons.LIGHT_MODE
            login.border = ft.border.all(1,'white')
            register.border = ft.border.all(1,'white')
            page.update()
        
        else:
            page.theme_mode = "light"
            theme_change.icon = ft.icons.DARK_MODE
            login.border = ft.border.all(1,'#084d0d')
            register.border = ft.border.all(1,'#084d0d')
            page.update()

    def login_method(u_name,u_password):
        if u_name.value == "" or u_password.value == "":
            alert("Warning","Incorrect Username or Password Try Again With Correct Details")
        else:
            check_permission()
            alert("Permission","Requesting Persmission")
        page.update()

    def register_method(r_name,r_cnic,r_email,r_phone,r_ntn,r_transaction):
        if r_name.value =="" or r_cnic.value =="" or r_email.value =="" or r_phone.value =="" or r_ntn.value =="" or r_transaction.value =="" :
            alert("Warning","Please Enter Complete Details")
        page.update()        

    theme_change = ft.IconButton(icon=ft.icons.DARK_MODE,icon_color='White',on_click= lambda _: switch_theme(theme_change))
    help_center = ft.IconButton(icon=ft.icons.HELP_CENTER,icon_color='White',on_click= lambda _: page.launch_url('https://miflexwave.com/contact-us/'))
    
    #file pickers
    def read_image_post(file_path):
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        return binary_data
    
    def pick_files_transaction(e: ft.FilePickerResultEvent):
        
        #selected_files1.value = (
        #    ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        #)

        r_transaction_img.style = ft.ButtonStyle(
                bgcolor='#084d0d',color='White',
                shape=ft.RoundedRectangleBorder(radius=10),
            )
        r_transaction_img.icon=ft.icons.CHECK
        r_transaction_img.update()
        page.update()

        print(e.data)
        data = e.data
        path_key = '"path":"'
        start_index = data.find(path_key) + len(path_key)
        end_index = data.find('"', start_index)
        
        # Extract the path value
        file_path = data[start_index:end_index]

        # Print the extracted path
        print(f"File Path: {file_path}")
        print(selected_files1.value)
        
        # Convert the file to binary data
        selected_files2.value = read_image_post(file_path)
        print(f"Binary Data: {selected_files2.value}...")  # Print the first 20 bytes for verification
        
        # Convert binary data to base64 string
        base64_data = base64.b64encode(selected_files1.value).decode('utf-8')
        
        # Set the image source
        tat = base64_data
        #print(tat)
        page.update()

    pick_files_dialog_post = ft.FilePicker(on_result=pick_files_transaction)
    selected_files1 = ft.Text(value="PKR 300/- Per Year As An App Charges \nEasypaisa : 0319 5129050")
    selected_files2 = ft.Text()
    page.overlay.append(pick_files_dialog_post)

    r_transaction_img = ft.FilledButton(
            "Upload Screenshot",icon=ft.icons.ERROR,
            style=ft.ButtonStyle(
                bgcolor='RED',color='White',
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            on_click=lambda _: pick_files_dialog_post.pick_files(
                        allow_multiple=True,
                        allowed_extensions=['png','jpg','jpeg'],
                    ),
        )

    #login
    u_name = ft.TextField(label="Enter User ID",icon=ft.icons.PERSON,border=ft.InputBorder.UNDERLINE)
    u_password = ft.TextField(label="Enter Password",password=True,can_reveal_password=True,icon=ft.icons.LOCK,border=ft.InputBorder.UNDERLINE)
    u_btn = ft.FilledButton(
            "LogIn Now",
            style=ft.ButtonStyle(
                bgcolor='#084d0d',color='White',
                shape=ft.RoundedRectangleBorder(radius=10),
            ),on_click= lambda _: login_method(u_name,u_password)
        )
    
    login = ft.Container(
        content=ft.Column(
            [
                ft.Text("Enter LogIn Details"),ft.Container(height=2),u_name,u_password,ft.Container(height=12),u_btn,
                ft.Container(height=2),ft.TextButton(text="Not A Member Register Now",style=ft.ButtonStyle(color=''),on_click= lambda _: page.go("/register"))
            ],
            horizontal_alignment="center",
            
        ),
        #bgcolor='#272bf5',
        width=400,padding=25,border_radius=16,border=ft.border.all(1,'#084d0d')
    )

    #register
    r_name = ft.TextField(label="Full Name",icon=ft.icons.PERSON,border=ft.InputBorder.UNDERLINE)
    r_cnic = ft.TextField(label="National ID",icon=ft.icons.CARD_MEMBERSHIP,border=ft.InputBorder.UNDERLINE)
    r_email = ft.TextField(label="Email",icon=ft.icons.MAIL,border=ft.InputBorder.UNDERLINE)
    r_phone = ft.TextField(label="WhatsApp No",icon=ft.icons.PHONE,border=ft.InputBorder.UNDERLINE)
    r_ntn = ft.TextField(label="National Tax No",icon=ft.icons.MONEY,border=ft.InputBorder.UNDERLINE)
    r_transaction = ft.TextField(label="Transaction ID",helper_text="PKR 300/- Per Year As An App Charges \nEasypaisa : 0319 5129050",icon=ft.icons.NUMBERS,border=ft.InputBorder.UNDERLINE)
    r_btn = ft.FilledButton(
            "Register Now",
            style=ft.ButtonStyle(
                bgcolor='#084d0d',color='White',
                shape=ft.RoundedRectangleBorder(radius=10),
            ),on_click= lambda _: register_method(r_name,r_cnic,r_email,r_phone,r_ntn,r_transaction)
        )
    
    register = ft.Container(
        content=ft.Column(
            [
                ft.Text("Enter Your Complete Details"),ft.Container(height=2),
                r_name,r_cnic,r_email,r_phone,r_ntn,ft.Container(height=2),ft.Column([r_transaction_img,selected_files1],width=400),
                ft.Container(height=12),r_btn,
                ft.Container(height=2),ft.TextButton(text="Already A Member LogIn Now",style=ft.ButtonStyle(color=''),on_click= lambda _: page.go("/"))
            ],
            horizontal_alignment="center",
            
        ),
        #bgcolor='#272bf5',
        width=400,padding=25,border_radius=16,border=ft.border.all(1,'#084d0d')
    )


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                    #leading=logo,
                    actions=[theme_change,help_center,ft.Container(width=15)],
                    title=ft.Text("AlBurak Services",color='white'), bgcolor='#084d0d'),
                    #logo,ft.Container(height=2),
                    login
                    #ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
                horizontal_alignment='center',vertical_alignment="center",
                bgcolor='',padding=16,
            )
        )
        if page.route == "/register":
            page.views.append(
                ft.View(
                    "/register",
                    [
                        ft.AppBar(
                        leading=ft.IconButton(icon=ft.icons.APP_REGISTRATION_ROUNDED,icon_color='white'),
                        actions=[theme_change,help_center,ft.Container(width=15)],
                        title=ft.Text("AlBurak Services",color='white'), bgcolor='#084d0d'),
                        register
                        #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/register")),
                    ],
                    horizontal_alignment='center',vertical_alignment="center",
                bgcolor='',padding=16,scroll="hidden"
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
// // Javas Script For Dashboard Sidebar
const body = document.querySelector("body"),
            sidebar = body.querySelector('.sidebar'),
            toggles = body.querySelector('.toggle'),
            mobileSidebarToggle = body.querySelector('.mobile-sidebar-toggle'),
            sidebarOverlay = body.querySelector('.sidebar-overlay'),
           
            modeSwitch = body.querySelector('.toggle-switch'),
            mode = body.querySelector('.mode'),
            modeText = body.querySelector('.mode-text'),
            switching= body.querySelector('.switch'),
            home = body.querySelector('.home');

            if (modeSwitch) {
                modeSwitch.addEventListener('click', ()=>{
                    body.classList.toggle('dark');
                    if(modeText){
                        if(body.classList.contains('dark')){
                            modeText.innerText = "Light Mode";
                        }
                        else{
                            modeText.innerText = "Dark Mode";
                        }
                    }
                });

                modeSwitch.addEventListener('click', ()=>{
                    if(sidebar){
                        sidebar.classList.toggle('dark-sidebar');
                    }
                });

                modeSwitch.addEventListener('click', ()=>{
                    if(mode){
                        mode.classList.toggle('mode-back');
                    }
                });

                modeSwitch.addEventListener('click', ()=>{
                    if(switching){
                        switching.classList.toggle('switching');
                    }
                });

                modeSwitch.addEventListener('click', ()=>{
                    if(toggles){
                        toggles.classList.toggle('toggles');
                    }
                });

                modeSwitch.addEventListener('click', ()=>{
                    if(home){
                        home.classList.toggle('homes');
                    }
                });
            }

            function toggleSidebar() {
                if (!sidebar) return;
                sidebar.classList.toggle('close');

                const isMobile = window.innerWidth <= 799;
                const isOpen = !sidebar.classList.contains('close');

                if (isMobile) {
                    if (sidebarOverlay) {
                        sidebarOverlay.classList.toggle('active', isOpen);
                    }
                    body.classList.toggle('sidebar-open-mobile', isOpen);
                } else {
                    if (sidebarOverlay) {
                        sidebarOverlay.classList.remove('active');
                    }
                    body.classList.remove('sidebar-open-mobile');
                }
            }

            if (toggles && sidebar) {
                toggles.addEventListener('click', toggleSidebar);
            }

            // Mobile sidebar toggle is handled in header2.html inline script.
            // Keep this file responsible for desktop chevron toggle only.

            //Profile Image change
            
    const imgInput = document.getElementById("imgInput");
    const profilePreview = document.getElementById("profilePreview");

    if (imgInput && profilePreview) {
        imgInput.addEventListener("change", function(){
            const file = this.files[0];
            if (file){
                profilePreview.src = URL.createObjectURL(file);
            }
        });
    }

// =========================Script For Student Form=================
function loadDistricts(){
    let province = document.getElementById("id_province").value;
    let district = document.getElementById("id_districts");
    
    district.innerHTML = "<option value=''>Select District</option>";

    let data = {
        // ======PUNJAB======
        Punjab :["Attock","Bahawalnagar","Bahawalpur","Bhakkar","Chakwal","Chiniot","Dera Ghazi Khan","Faisalabad","Gujranwala","Gujrat","Hafizabad","Jhang","Jhelum","Kasur","Khanewal","Khushab","Kot Addu","Lahore","Layyah","Lodhran","Mandi Bahauddin","Mianwali","Multan","Muree","Muzaffargarh","Narowal","Nankana Sahib","Okara","Pakpattan","Rahim Yar Khan","Rajanpur","Rawalpindi","Sahiwal","Sargodha","Sheikhupura","Sialkot","Talagang","Taunsa","Toba Tek Singh","Vehari","Wazirabad"],

        // ============SINDH==========
      Sindh : ["Badin","Dadu","Ghotki","Hyderabad","Jacobabad","Jamshoro","Karachi Central","Karachi East","Karachi South","Karachi West","Kashmore","Keamari","Khairpur","Korangi","Larkana","Malir","Matiari","Mirpur Khas","Naushahro Feroze","Qambar Shahdadkot","Sanghar","Shaheed Benazirabad","Shikarpur","Sukkur","Sujawal","Tando Allahyar","Tando Muhammad Khan","Thatta","Tharparkar","Umerkot"],

    //   ============KHYBER PAKHTUNKHAWA============
    khyber_pakhtunkhwa:["Abbottabad","Bajaur","Bannu","Battagram","Buner","Charsadda","Chitral Lower","Chitral Upper","Dera Ismail Khan","Hangu","Haripur","Karak","Khyber","Kohat","Kolai Palas","Kurram","Lakki Marwat","Lower Dir","Lower Kohistan","Malakand","Mansehra","Mardan","Mohmand","North Waziristan","Nowshera","Orakzai","Peshawar","Shangla","South Waziristan","Swabi","Swat","Tank","Torghar","Upper Dir","Upper Kohistan"],

    Balochistan : ["Awaran","Barkhan","Chagai","Dera Bugti","Duki","Gwadar","Harnai","Hub","Jhal Magsi","Kachhi","Kalat","Kech","Kharan","Khuzdar","Kohlu","Lasbela","Loralai","Mastung","Musakhel","Nasirabad","Nushki","Panjgur","Pishin","Quetta","Qila Abdullah","Qila Saifullah","Sherani","Sibi","Sohbatpur","Surab","Usta Muhammad","Washuk","Zhob","Ziarat"],
    }

    if(province !== ""){
        data[province].forEach(function(item) {
            let option = document.createElement("option");
            option.value = item;
            option.text = item;
            district.appendChild(option);
        })
    }
   
}

// -------Change colors of div card left side border on Progress Outlines Page-----




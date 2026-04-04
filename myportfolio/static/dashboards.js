// // Javas Script For Dashboard Sidebar
const body = document.querySelector("body"),
            sidebar = body.querySelector('.sidebar'),
            toggles = body.querySelector('.toggle'),
           
            modeSwitch = body.querySelector('.toggle-switch'),
            mode = body.querySelector('.mode'),
            modeText = body.querySelector('.mode-text'),
            switching= body.querySelector('.switch'),
            home = body.querySelector('.home');

            modeSwitch.addEventListener('click', ()=>{
                body.classList.toggle('dark');
                if(body.classList.contains('dark')){
                    modeText.innerText = "Light Mode";
                }
                else{
                     modeText.innerText = "Dark Mode";
                }
            });

            modeSwitch.addEventListener('click', ()=>{
                sidebar.classList.toggle('dark-sidebar');
            });

            modeSwitch.addEventListener('click', ()=>{
                mode.classList.toggle('mode-back');
            });

            modeSwitch.addEventListener('click', ()=>{
                switching.classList.toggle('switching');
            });

            modeSwitch.addEventListener('click', ()=>{
                searchBtn.classList.toggle('mode-back');
            });

            modeSwitch.addEventListener('click', ()=>{
                toggles.classList.toggle('toggles');
            });
            modeSwitch.addEventListener('click', ()=>{
                home.classList.toggle('homes');
            });
          
            toggles.addEventListener('click', ()=>{
                sidebar.classList.toggle('close');
            });

            //Profile Image change
            
    document.getElementById("imgInput").addEventListener("change", function(){
        const file = this.files[0];
        if (file){
        document.getElementById("profilePreview").src = URL.createObjectURL(file);
         }
    });

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




// This is for what will happens when user will clcik the 'login as guest' this button



const toastTrigger = document.getElementById('guestToastBtn')
const toastLiveExample = document.getElementById('guestToast')

if (toastTrigger) {
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    toastTrigger.addEventListener('click', () => {
        toastBootstrap.show()
    })
}

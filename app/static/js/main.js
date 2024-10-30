const  getTitleMessageFromCategory = category => {
    const titles = {
        'success': '¡Bien hecho!',
        'info': '¡ATENCIÓN!',
        'warning': '¡ATENCIÓN!',
        'error': 'Oops...'
    }

    return titles[category];
}

function showMessageAlert(category, message) {
    Swal.fire({
        icon: category,
        title: getTitleMessageFromCategory(category),
        text: message
      });
}
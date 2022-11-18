/*$('#show_confirmation').click(function(id) {
    Swal.fire({
      title: '¿Está seguro?',
      text: "No podrá revertir la acción",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      cancelButtonText: 'Cancelar.',
      confirmButtonText: 'Si.'
    }).then((result) => {
      if (result.isConfirmed) {       
        $(
          '#send'
        ).submit();
      }
    })


  }) */

  $.confirmation = function(id) {
    
    Swal.fire({
      title: '¿Está seguro?',
      text: "No podrá revertir la acción",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      cancelButtonText: 'Cancelar.',
      confirmButtonText: 'Si.'
    }).then((result) => {
      if (result.isConfirmed) {       
        $(
          id
        ).submit();
      }
    })
 };
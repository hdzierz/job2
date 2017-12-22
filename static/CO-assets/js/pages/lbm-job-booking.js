//------------- lbm-jobs-booking.js -------------//
$(document).ready(function() {

    
    // -------- add validation to form wizard ---//
    var $validator = $("#wizard1 form").validate({
        errorPlacement: function( error, element ) {
            var place = element.closest('.input-group');
            if (!place.get(0)) {
                place = element;
            }
            if (place.get(0).type === 'checkbox') {
                place = element.parent();
            }
            if (error.text() !== '') {
                place.after(error);
            }
        },
        errorClass: 'help-block',
        rules: {
            email: {
                required: true,
                email: true
            },
            username: {
                required: true
            },
            password: {
                required: true,
                minlength: 5
            },
            password_2: {
                required: true,
                minlength: 5,
                equalTo: "#password"
            }
        },
        messages: {
            purchase_no: {
                required: "Please put dwoih  in the purchase #."
            },
            email: {
                required: "Please put in your email."
            }
        },
        highlight: function( label ) {
            $(label).closest('.form-group').removeClass('has-success').addClass('has-error');
        },
        success: function( label ) {
            $(label).closest('.form-group').removeClass('has-error');
            label.remove();
        }
    });
	
});

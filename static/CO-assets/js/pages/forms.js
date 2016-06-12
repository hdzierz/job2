//------------- tables-data.js -------------//
$(document).ready(function() {


	// JS from advanced forms...
	    //------------- Fancy select -------------//
    $('.fancy-select').fancySelect();
    //custom templating
    $('.fancy-select1').fancySelect({
        optionTemplate: function(optionEl) {
            return optionEl.text() + '<i class="pull-left ' + optionEl.data('icon') + '"></i>';
        }
    });

	//------------- Select 2 -------------//
	$('.select2').select2({placeholder: 'Start typing'});

	//minumum 2 symbols input
	$('.select2-minimum').select2({
		placeholder: 'Start typing',
		minimumInputLength: 2,
	});

	//------------- Masked input fields -------------//
	// $("#mask-phone").mask("(999) 999-9999", {completed:function(){alert("Callback action after complete");}});
	// $("#mask-phoneExt").mask("(999) 999-9999? x99999");
	// $("#mask-phoneInt").mask("+40 999 999 999");
	// $("#mask-date").mask("99/99/9999");
	// $("#mask-ssn").mask("999-99-9999");
	// $("#mask-productKey").mask("a*-999-a999", { placeholder: "*" });
	// $("#mask-eyeScript").mask("~9.99 ~9.99 999");
	// $("#mask-percent").mask("99%");

	//------------- Dual list box -------------//
	// $('.duallistbox').bootstrapDualListbox({
	//     nonSelectedListLabel: 'Non-selected',
 //  		selectedListLabel: 'Selected',
	//     preserveSelectionOnMove: 'moved',
	//     moveOnSelect: false,
	// });

	// //------------- Spinners -------------//
	// $("#basic-spinner").TouchSpin({
 //      min: 0,
 //      max: 100
 //  });
 //  //with postfix
 //  $("#postfix-spinner").TouchSpin({
 //      min: 0,
 //      max: 100,
 //      postfix: '%'
 //  });
 //  //with prefix
 //  $("#prefix-spinner").TouchSpin({
 //      min: 0,
 //      max: 100,
 //      prefix: '$'
 //  });
 //  //decimal spinner
 //  $("#decimal-spinner").TouchSpin({
 //      min: 1,
 //      max: 10,
 //      step: 0.1,
 //      decimals: 2
 //  });
 //  //vertical buttons
 //  $("#vertical-spinner").TouchSpin({
 //      verticalbuttons: true,
 //      verticalupclass: 'fa fa-angle-up s12',
 //      verticaldownclass: 'fa fa-angle-down s12'
 //  });

  //------------- Datepicker -------------//
  $("#basic-datepicker").datepicker();

  // generic date-picker class
  $(".basic-datepicker").datepicker();
  $(".CO-datepicker").datepicker();

  //multiple date
  $("#multiple-datepicker").datepicker({
  	multidate: true
  });
  //date range
  $(".input-daterange").datepicker();
  //inline
  $("#inline-datepicker").datepicker();

  //------------- Tags -------------//
  //from json
  var citynames = new Bloodhound({
	  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
	  queryTokenizer: Bloodhound.tokenizers.whitespace,
	  prefetch: {
	    url: 'ajax/citynames.json',
	    filter: function(list) {
	      return $.map(list, function(cityname) {
	        return { name: cityname }; });
	    }
	  }
	});
	citynames.initialize();

	$('#json-tags').tagsinput({
		typeaheadjs: {
			name: 'citynames',
			displayKey: 'name',
			valueKey: 'name',
			source: citynames.ttAdapter()
		}
	});
	
});
//------------- forms-wizard.js -------------//
$(document).ready(function() {

   //------------- Form wizard -------------//

  //init first wizard
  $('#wizard').bootstrapWizard({
      tabClass: 'bwizard-steps',
      nextSelector: 'ul.pager li.next',
      previousSelector: 'ul.pager li.previous',
      firstSelector: null,
      lastSelector: null,
      onNext: function( tab, navigation, index, newindex ) {
          var validated = $('#wizard form').valid();
          if( !validated ) {
              $validator.focusInvalid();
              return false;
          }
      },
      onTabClick: function( tab, navigation, index, newindex ) {
          if ( newindex == index + 1 ) {
              return this.onNext( tab, navigation, index, newindex);
          } else if ( newindex > index + 1 ) {
              return false;
          } else {
              return true;
          }
      },
      onTabShow: function( tab, navigation, index ) {
          tab.prevAll().addClass('completed');
          tab.nextAll().removeClass('completed');
          var $total = navigation.find('li').length;
          var $current = index+1;
          // If it's the last tab then hide the last button and show the finish instead
          if($current >= $total) {
              $('#wizard').find('.pager .next').hide();
              $('#wizard').find('.pager .finish').show();
              $('#wizard').find('.pager .finish').removeClass('disabled');
          } else {
              $('#wizard').find('.pager .next').show();
              $('#wizard').find('.pager .finish').hide();
          }
      }
  });

  //wizard is finish
  $('#wizard .finish').click(function() {
      //show message
  });

  //------------- Wizard with progressbar -------------//
  //init first wizard
  $('#wizard1').bootstrapWizard({
      tabClass: 'bwizard-steps',
      nextSelector: 'ul.pager li.next',
      previousSelector: 'ul.pager li.previous',
      firstSelector: null,
      lastSelector: null,
      onTabShow: function( tab, navigation, index ) {
          tab.prevAll().addClass('completed');
          tab.nextAll().removeClass('completed');
          var $total = navigation.find('li').length;
          var $current = index+1;
          var $percent = ($current/$total) * 100;
          $('#wizard1').find('.progress-bar').css({width:$percent+'%'});
          // If it's the last tab then hide the last button and show the finish instead
          if($current >= $total) {
              $('#wizard1').find('.pager .next').hide();
              $('#wizard1').find('.pager .finish').show();
              $('#wizard1').find('.pager .finish').removeClass('disabled');
          } else {
              $('#wizard1').find('.pager .next').show();
              $('#wizard1').find('.pager .finish').hide();
          }
      }
  });

  //wizard is finish
  $('#wizard1 .finish').click(function() {
      //show message
  });

});
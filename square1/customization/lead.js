frappe.ui.form.on("Lead",{ 
	refresh: function(frm) {
		var me = this
		if(!frm.doc.__islocal && frm.doc.status == "Converted") {		
				cur_frm.add_custom_button(__('Order Form'), function() {
				cur_frm.cscript.make_order(); 
				}, __("Make"));
				cur_frm.page.set_inner_btn_group_as_primary(__("Make"));
		}
	}
});

cur_frm.cscript.make_order =function(){
	frappe.model.open_mapped_doc({
		method: "square1.customization.lead.make_order",
		frm: cur_frm
	});
}
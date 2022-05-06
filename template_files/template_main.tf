resource "genesyscloud_integration_action" "action" {
    name           = var.action_name
    category       = var.action_category
    integration_id = var.integration_id
    secure         = var.secure_data_action
    
    contract_input  = contract_input_placeholder
    contract_output = contract_output_placeholder
    
    config_request {
        request_template     = "request_template_placeholder"
        request_type         = "request_type_placeholder"
        request_url_template = "request_url_template_placeholder"
        headers_placeholder
    }

    config_response {
        success_template = "success_template_placeholder"
        translation_map_placeholder 
        translation_map_defaults_placeholder       
    }
}
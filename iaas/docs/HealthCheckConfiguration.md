# HealthCheckConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The protocol used for the health check. | 
**port** | **str** | Port on the back-end instance machine to use for the health check. | 
**url_path** | **str** | URL path on the back-end instance against which a request will be performed for the health check. Useful when the health check protocol is HTTP/HTTPS. | [optional] 
**interval_seconds** | **int** | Interval (in seconds) at which the health checks will be performed. | [optional] 
**timeout_seconds** | **int** | Timeout (in seconds) to wait for a response from the back-end instance. | [optional] 
**unhealthy_threshold** | **int** | Number of consecutive check failures before considering a particular back-end instance as unhealthy. | [optional] 
**healthy_threshold** | **int** | Number of consecutive successful checks before considering a particular back-end instance as healthy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


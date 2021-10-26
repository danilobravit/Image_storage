# Image_storage

### Instruction
If you want to add an image from a URL please follow steps below.
1. Add "id" field. This field must be ONLY incremented by 1 in reference to the id of previos image.
2. Add "image_url" field. This is link to your image.
3. "download_link" will be generated automaticly after POST request.

### Example
Before POST
```
{
    "id": 20,
    "image_url": "https://as2.ftcdn.net/v2/jpg/04/42/18/09/1000_F_442180940_X33IWFdiZrkRHCGChEdvzY9EMKT9gImi.jpg",
   
}
```
After POST
```
{
    "id": 20,
    "image_url": "https://as2.ftcdn.net/v2/jpg/04/42/18/09/1000_F_442180940_X33IWFdiZrkRHCGChEdvzY9EMKT9gImi.jpg",
    "download_url": "http://127.0.0.1:8000/20/download"
}
```
### ATTENTION!
Values of "id" field and value after your local hos IP in "download_url" should be the same!!! 
If you want to download image directly from URL field in your browser, enter "http://your_local_host_IP/id_of_image/download" (ex. http://127.0.0.1:8000/20/download).

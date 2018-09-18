# Some POC used by mongoDB

## POC List

### Group Notice

- Model
    - Old:
        ```json
        GroupNoticeOld:
        {
          "unrecieved": {
            "school_id": {
              "group_id": {
                "class_id": [1, 2, 3, ..., n]
              }
            }
          },
          "hasrecieved": {
            "school_id": {
              "group_id": {
                "class_id": []
              }
            }
          }
        }
        ```
    - New:
        ```json
        Notice:
        {
          "school_id": 1,
          "group_id": 2,
          "class_id": 3,
          "unrecieved": [1, 2, 3, ..., n],
          "hasrecieved": [1, 2, 3, ..., n],
        }
        ```
- API
    - `/notice/old`
        ```js
        data = {
          "sid": 1, // school id
          "gid": 2, // group id
          "cid": 3, // class id
          "nid": 1 // notice id
        }
        method = 'PUT'
        ```
    - `/notice/new`
        ```js
        data = {
          "sid": 1, // school id
          "gid": 2, // group id
          "cid": 3, // class id
          "nid": 1 // notice id
        }
        method = 'PUT'
        ```
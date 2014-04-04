DROP TABLE ejam;

CREATE TABLE ejam
(
    index_id      bigint,    -- Example: 13
    network       varchar,   -- Example: eJam
    app_id        varchar,   -- Example: e2ef288479fa11e295fa123138070049
    adunit_id     varchar,   -- Example: 19aa68ca85b311e295fa123138070049
    country       varchar,   -- Example: US
    udid          varchar,   -- Example: CkBUJJcZKmmr1rZgSeZE
    req_id        varchar,   -- Example: 6d50f266fad211e290bc0025907b585f
    time_stamp    timestamp, -- Example: 2013-08-01 17:47:26
    sdk_version   varchar,   -- Example: None
    os_version    varchar,   -- Example: 6.1.3
    carrier       varchar,   -- Example: None
    request_url   varchar,   -- Example: http://r.tapit.com/adrequest.php?zone=22443&format=json&ip=69.133.14.224&w=300&h=250&ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329
    response_code bigint,    -- Example: 200
    response_body varchar,   -- Example: {"type":"banner","html":"<a href=\"http:\/\/c.tapit.com\/adclick.php?zone=22443&amp;cid=155781&amp;adtype=11&amp;w=300&amp;h=250&amp;xid=304c2a379270184fb4aa0b60eab9cbb2&amp;ip=69.133.14.224&amp;udid=&amp;adnetwork=1&amp;ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329&amp;track_urls=\" target=\"_blank\"><img src=\"http:\/\/i.tapit.com\/adimage.php?zone=22443&amp;cid=155781&amp;adtype=11&amp;xid=304c2a379270184fb4aa0b60eab9cbb2&amp;ip=69.133.14.224&amp;udid=&amp;ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329&amp;adnetwork=1&amp;w=300&amp;h=250\" width=\"300\" height=\"250\" alt=\"\"\/><\/a>","adId":"155781","adWidth":"300","adHeight":"250","cpc":0.07,"adtitle":"","adtext":"","clickurl":"http:\/\/c.tapit.com\/adclick.php?zone=22443&cid=155781&adtype=11&w=300&h=250&xid=304c2a379270184fb4aa0b60eab9cbb2&ip=69.133.14.224&udid=&adnetwork=1&ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329&track_urls=","imageurl":"http:\/\/i.tapit.com\/adimage.php?zone=22443&cid=155781&adtype=11&xid=304c2a379270184fb4aa0b60eab9cbb2&ip=69.133.14.224&udid=&ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329&adnetwork=1&w=300&h=250","domain":"c.tapit.com"}
    is_valid_ad   boolean,   -- Example:
    dayofweek     bigint,    -- Example: 3
    hour          bigint,    -- Example: 17
    adWidth       bigint,    -- Example: 300
    cpc           real,      -- Example: 0.07
    cpm           real,      -- Example:
    imageurl      varchar,   -- Example: http://i.tapit.com/adimage.php?zone=22443&cid=155781&adtype=11&xid=304c2a379270184fb4aa0b60eab9cbb2&ip=69.133.14.224&udid=&ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329&adnetwork=1&w=300&h=250
    clickurl      varchar,   -- Example: http://c.tapit.com/adclick.php?zone=22443&cid=155781&adtype=11&w=300&h=250&xid=304c2a379270184fb4aa0b60eab9cbb2&ip=69.133.14.224&udid=&adnetwork=1&ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329&track_urls=
    adtext        varchar,   -- Example:
    domain        varchar,   -- Example: c.tapit.com
    adHeight      bigint,    -- Example: 250
    html          varchar,   -- Example: <a href="http://c.tapit.com/adclick.php?zone=22443&amp;cid=155781&amp;adtype=11&amp;w=300&amp;h=250&amp;xid=304c2a379270184fb4aa0b60eab9cbb2&amp;ip=69.133.14.224&amp;udid=&amp;adnetwork=1&amp;ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329&amp;track_urls=" target="_blank"><img src="http://i.tapit.com/adimage.php?zone=22443&amp;cid=155781&amp;adtype=11&amp;xid=304c2a379270184fb4aa0b60eab9cbb2&amp;ip=69.133.14.224&amp;udid=&amp;ua=Mozilla%2F5.0+%28iPad%3B+CPU+OS+6_1_3+like+Mac+OS+X%29+AppleWebKit%2F536.26+%28KHTML%2C+like+Gecko%29+Mobile%2F10B329&amp;adnetwork=1&amp;w=300&amp;h=250" width="300" height="250" alt=""/></a>
    adId          bigint,    -- Example: 155781
    adtitle       varchar,   -- Example:
    type          varchar,   -- Example: banner
    xid           varchar,   -- Example: 304c2a379270184fb4aa0b60eab9cbb2
    zone          bigint,    -- Example: 22443
    cid           bigint,    -- Example: 155781
    h             varchar,   -- Example: 250" width="300" height="250" alt=""/></a>
    track_urls    varchar,   -- Example: " target="_blank"><img src="http://i.tapit.com/adimage.php?zone=22443
    w             varchar,   -- Example: 300
    ip            varchar,   -- Example: 69.133.14.224
    adtype        bigint,    -- Example: 11
    ua            varchar,   -- Example: Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329
    adnetwork     bigint,    -- Example: 1
    device_model  varchar    -- Example: iPad
);

COPY ejam FROM '/tmp/data_ejam.sample.csv' DELIMITER ',' CSV;



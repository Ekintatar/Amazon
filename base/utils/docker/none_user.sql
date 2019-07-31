INSERT INTO spPanel.cityList (
	id,
	geoname_id,
	locale_code,
	continent_code,
	continent_name,
	country_iso_code,
	country_name,
	subdivision_1_iso_code,
	subdivision_1_name,
	subdivision_2_iso_code,
	subdivision_2_name,
	city_name,
	metro_code,
	time_zone 
)
VALUES
	(
		14839,
		'1679207',
		'en',
		'AS',
		'Asia',
		'TW',
		'Taiwan',
		'YUN',
		'Yunlin County',
		'',
		'',
		'Adan',
		'',
		'Asia/Taipei' 
	) 
	ON DUPLICATE KEY UPDATE locale_code = 'en';
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		72,
		'Selenium',
		'Selenium',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'selenium@useinsider.com',
		'developer',
		1,
		'',
		'en',
		1,
		0,
		0,
		1,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		1455,
		'Selenium',
		'Test',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'collaborate@mail.com',
		'',
		1,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		1454,
		'Test',
		'Test',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'view@mail.com',
		'',
		1,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		2785,
		'Test',
		'Test',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'outsource@mail.com',
		'',
		1,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		1456,
		'Selenium',
		'Test',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'norole@mail.com',
		'',
		1,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		1457,
		'Selenium',
		'Test',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'norole.deactive@mail.com',
		'',
		0,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		1458,
		'Selenium',
		'Test',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'hasrole.deactive@mail.com',
		'',
		0,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		1461,
		'Selenium',
		'Test',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'selenium@mail.com',
		'',
		1,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		3217,
		'selenium',
		'locked',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'lock@mail.com',
		'',
		1,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		0 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
INSERT INTO spPanel.users (
	id,
	NAME,
	surname,
	PASSWORD,
	email,
	unvan,
	isActive,
	remember_token,
	LANGUAGE,
	isInsiderEmployee,
	isSuperAdmin,
	isAuthorized,
	accessAreaPermission,
	passwordExpiryDate,
	failedLoginCount 
)
VALUES
	(
		3218,
		'selenium',
		'lock',
		'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
		'lock_threshold@mail.com',
		'',
		1,
		'',
		'en',
		0,
		0,
		0,
		0,
		NOW( ) + INTERVAL 30 DAY,
		2 
	) 
	ON DUPLICATE KEY UPDATE PASSWORD = 'e39d05b72f25767869d44391919434896bb055772d7969f74472032b03bc18418911f3b0e6dd47ff8f3b2323728225286c3cb36914d28dc7db40bdd786159c0a',
	passwordExpiryDate = NOW( ) + INTERVAL 30 DAY;
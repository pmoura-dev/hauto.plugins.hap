CREATE TABLE "HAPAccessory"
(
    "device_id" INTEGER PRIMARY KEY,
    "accessory" VARCHAR(50),

    CONSTRAINT fk_device_id
        FOREIGN KEY ("device_id")
            REFERENCES "Device" ("id")
);


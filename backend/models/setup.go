package models

import (
	"log"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var DB *gorm.DB

func ConnectDatabase() {
	database, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		log.Fatal("Failed to conenct to database")
	}

	if err := database.AutoMigrate(&User{}); err != nil {
		log.Fatal(err)
	}

	DB = database
}

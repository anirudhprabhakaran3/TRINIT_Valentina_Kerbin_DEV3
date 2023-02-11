package services

import (
	"errors"
	"fmt"
	"time"

	"github.com/anirudhprabhakaran3/TRINIT_Valentina_Kerbin_DEV3/backend/models"
	"github.com/dgrijalva/jwt-go"
)

var jwtKey = []byte("I4zXN5MlDdyLFuxxHjdAUBNHaFU+qKOwH3emPxIoEIaVVEafz5NOWlu/7btM38xKNM9QYn4pV+N65gWJD0qMUG/UFmgSZOALaewkLWDD3EjM+fJR9ZbNlFQO78lOP6BZ.YMPjY2okkOMD5MaW0C4wajJk9ZPVY/qHBOB60KjxqZhII7BcOmcIijZ2h6qIRFUuN4RntiS46oy/n6K6YTyZBvKaSsP/hml2fZLLqA==")

type authClaims struct {
	jwt.StandardClaims
	UserID uint `json:"userID"`
}

func GenerateToken(user models.User) (string, error) {
	expiresAt := time.Now().Add(24 * time.Hour).Unix()
	token := jwt.NewWithClaims(jwt.SigningMethodHS512, authClaims{
		StandardClaims: jwt.StandardClaims{
			Subject:   user.Username,
			ExpiresAt: expiresAt,
		},
		UserID: user.ID,
	})

	tokenString, err := token.SignedString(jwtKey)
	if err != nil {
		return "", err
	}
	return tokenString, nil
}

func ValidateToken(tokenString string) (uint, string, error) {
	var claims authClaims
	token, err := jwt.ParseWithClaims(tokenString, &claims, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["ald"])
		}
		return jwtKey, nil
	})
	if err != nil {
		return 0, "", err
	}

	if !token.Valid {
		return 0, "", errors.New("invalid token")
	}

	id := claims.UserID
	username := claims.Subject
	return id, username, nil
}

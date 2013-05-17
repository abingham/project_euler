module Main where

import Text.ParserCombinators.Parsec

import Array
import Data.Char
import Data.Maybe

run :: Show a => Parser a -> String -> IO ()
run p input
    = case (parse p "" input) of
        Left err -> do{ putStr "parse error at "
                      ; print err
                      }
        Right x  -> print x

integer :: Parser String
integer = many1 digit

integers :: Parser [String]
-- TODO: This doesn't handle trailing white space. How? Look at lexer system, etc.
integers = do { ints <- sepBy integer (skipMany space)
              ; skipMany space
              ; return ints
              }

stringToInt :: String -> Int
stringToInt s = foldl (\z x -> z * 10 + (digitToInt x)) 0 s 

parseInts :: String -> [Int]
parseInts input
    = case (parse integers "" input) of
        -- Left err -> Nothing
        Right x -> map stringToInt x

intMatrix :: [Int] -> Array (Int, Int) Int 
intMatrix input = array ((0,0), (19,19)) [((x,y), input!!(x + y * 20)) | y <- [0..19], x <- [0..19]]

xdim = 20
ydim = 20

val :: [Int] -> Int -> Int -> Int
val mtx x y = mtx!!(x + y * xdim)

vert :: [Int] -> Int -> Int -> Int
vert mtx x y = val mtx x y + val mtx x (y + 1) + val mtx x (y + 2) + val mtx x (y + 3)

verts :: [Int] -> [Int]
verts mtx = [vert mtx x y | x <- [0..20], y <- [0..17]]

solve :: Array (Int, Int) Int -> IO()
solve x = print x

-- TODO: Look at Ix array library for matrix support

main = do
  -- run sentence "Hello there."
  input <- readFile "euler_11.input"
  solve $ intMatrix $ parseInts input
 
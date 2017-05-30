# Perform alignment usign muscle
for filename in "$@"
do
    muscle -in $filename -out $filename-align.afa
done

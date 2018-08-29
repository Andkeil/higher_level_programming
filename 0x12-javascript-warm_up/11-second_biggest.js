#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = [];
  for (let i = 3; i <= process.argv.length; i++) {
    args.push(parseInt(process.argv[i - 1]));
  } console.log(args.sort().reverse()[1]);
}

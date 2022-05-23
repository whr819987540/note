vscode导出扩展列表并安装

```bash
code --list-extensions vs_code_extensions_list.txt
cat vs_code_extensions_list.txt | xargs -n 1 code --install-extension
```


import sublime, sublime_plugin
import re

# Provide completions that match just after typing an opening angle bracket
# based on html_completions.py and visualforce completions by 
# github.com/jairzh/sublime-sfdc-assist/blob/master/visualforce_completions.py
class VisualforceCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0],
                "text.html.visualforce"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '<':
            return []

        return ([
            ("apex:actionFunction\tVisualforce", "apex:actionFunction name=\"$1\" action=\"$2\" rerender=\"$3\" status=\"$4\"/>"),
            ("apex:actionPoller\tVisualforce", "apex:actionPoller action=\"$1\" rerender=\"$2\" interval=\"$3\"/>"),
            ("apex:actionRegion\tVisualforce", "apex:actionRegion>\n\t$1\n</apex:actionRegion>"),
            ("apex:actionStatus\tVisualforce", "apex:actionStatus id=\"$1\"/>"),
            ("apex:actionSupport\tVisualforce", "apex:actionSupport event=\"$1\" action=\"$2\" rerender=\"$3\" status=\"$4\"/>"),
            ("apex:attribute\tVisualforce", "apex:attribute name=\"$1\" description=\"$2\" type=\"$3\" required=\"${4:true}\"/>"),
            ("apex:column\tVisualforce", "apex:column value=\"$1\"/>"),
            ("apex:commandButton\tVisualforce", "apex:commandButton action=\"$1\" value=\"$2\" id=\"$3\"/>"),
            ("apex:commandLink\tVisualforce", "apex:commandLink action=\"$1\" value=\"$2\" id=\"$3\"/>"),
            ("apex:component\tVisualforce", "apex:component>\n\t$1\n</apex:component>"),
            ("apex:componentBody\tVisualforce", "apex:componentBody />"),
            ("apex:composition\tVisualforce", "apex:composition template=\"$1\">\n\t$2\n</apex:composition>"),
            ("apex:dataList\tVisualforce", "apex:dataList value=\"$1\" var=\"$2\" id=\"$3\">\n\t$4\n</apex:dataList>"),
            ("apex:dataTable\tVisualforce", "apex:dataTable value=\"$1\" var=\"$2\" id=\"$3\">\n\t$4\n</apex:dataTable>"),
            ("apex:define\tVisualforce", "apex:define name=\"$1\"/>"),
            ("apex:detail\tVisualforce", "apex:detail subject=\"$1\" relatedList=\"${2:false}\" title=\"${3:false}\"/>"),
            ("apex:dynamicComponent\tVisualforce", "apex:dynamicComponent componentValue=\"$1\"/>"),
            ("apex:emailPublisher\tVisualforce", "apex:emailPublisher />"),
            ("apex:enhancedList\tVisualforce", "apex:enhancedList type=\"$1\" height=\"$2\" rowsPerPage=\"$3\" id=\"$4\"/>"),
            ("apex:facet\tVisualforce", "apex:facet name=\"$1\">$2<apex:facet/>"),
            ("apex:flash\tVisualforce", "apex:flash src=\"$1\" height=\"$2\" width=\"$3\"/>"),
            ("apex:form\tVisualforce", "apex:form id=\"$1\">\n\t$2\n</apex:form>"),
            ("apex:iframe\tVisualforce", "apex:iframe src=\"$1\" scrolling=\"$2\" id=\"$3\"/>"),
            ("apex:image\tVisualforce", "apex:image id=\"$1\" value=\"$2\" width=\"$3\" height=\"$4\"/>"),
            ("apex:include\tVisualforce", "apex:include pageName=\"$1\"/>"),
            ("apex:includeScript\tVisualforce", "apex:includeScript value=\"$1\"/>"),
            ("apex:inlineEditSupport\tVisualforce", "apex:inlineEditSupport showOnEdit=\"$1\" cancelButton=\"$2\" hideOnEdit=\"$3\" event=\"$4\"/>"),
            ("apex:inputCheckbox\tVisualforce", "apex:inputCheckbox value=\"$1\"/>"),
            ("apex:inputField\tVisualforce", "apex:inputField value=\"$1\"/>"),
            ("apex:inputHidden\tVisualforce", "apex:inputHidden value=\"$1\"/>"),
            ("apex:inputSecret\tVisualforce", "apex:inputSecret value=\"$1\"/>"),
            ("apex:inputText\tVisualforce", "apex:inputText value=\"$1\"/>"),
            ("apex:inputTextarea\tVisualforce", "apex:inputTextarea value=\"$1\"/>"),
            ("apex:insert\tVisualforce", "apex:insert name=\"$1\"/>"),
            ("apex:listViews\tVisualforce", "apex:listViews name=\"$1\"/>"),
            ("apex:message\tVisualforce", "apex:message for=\"$1\"/>"),
            ("apex:messages\tVisualforce", "apex:messages />"),
            ("apex:outputField\tVisualforce", "apex:outputField value=\"$1\"/>"),
            ("apex:outputLabel\tVisualforce", "apex:outputLabel value=\"$1\" for=\"$2\"/>"),
            ("apex:outputLink\tVisualforce", "apex:outputLink value=\"$1\"/>"),
            ("apex:outputPanel\tVisualforce", "apex:outputPanel id=\"$1\">\n\t$2\n</apex:outputPanel>"),
            ("apex:outputText\tVisualforce", "apex:outputText value=\"$1\"/>"),
            ("apex:page\tVisualforce", "apex:page id=\"$1\">\n\t$2\n</apex:page>"),
            ("apex:pageBlock\tVisualforce", "apex:pageBlock mode=\"${1:detail}\">\n\t$2\n</apex:pageBlock>"),
            ("apex:pageBlockButtons\tVisualforce", "apex:pageBlockButtons>\n\t$1\n</apex:pageBlockButtons>"),
            ("apex:pageBlockSection\tVisualforce", "apex:pageBlockSection title=\"$1\" columns=\"$2\">\n\t$3\n</apex:pageBlockSection>"),
            ("apex:pageBlockSectionItem\tVisualforce", "apex:pageBlockSectionItem>\n\t$1\n</apex:pageBlockSectionItem>"),
            ("apex:pageBlockTable\tVisualforce", "apex:pageBlockTable value=\"$1\" var=\"$2\">\n\t$3\n</apex:pageBlockTable>"),
            ("apex:pageMessage\tVisualforce", "apex:pageMessage summary=\"$1\" serverity=\"$2\" strength=\"${3:3}\"/>"),
            ("apex:pageMessages\tVisualforce", "apex:pageMessages />"),
            ("apex:panelBar\tVisualforce", "apex:panelBar>\n\t$1\n</apex:panelBar>"),
            ("apex:panelBarItem\tVisualforce", "apex:panelBarItem label=\"$1\">$2<apex:panelBarItem/>"),
            ("apex:panelGrid\tVisualforce", "apex:panelGrid columns=\"$1\">\n\t$2\n</apex:panelGrid>"),
            ("apex:panelGroup\tVisualforce", "apex:panelGroup id=\"$1\">\n\t$2\n</apex:panelGroup>"),
            ("apex:param\tVisualforce", "apex:param value=\"$1\"/>"),
            ("apex:relatedList\tVisualforce", "apex:relatedList list=\"$1\"/>"),
            ("apex:repeat\tVisualforce", "apex:repeat value=\"$1\" var=\"$2\">\n\t$3\n</apex:repeat>"),
            ("apex:selectCheckboxes\tVisualforce", "apex:selectCheckboxes value=\"$1\">\n\t$2\n</apex:selectCheckboxes>"),
            ("apex:selectList\tVisualforce", "apex:selectList value=\"$1\" size=\"$2\">\n\t$3\n</apex:selectList>"),
            ("apex:selectOption\tVisualforce", "apex:selectOption itemValue=\"$1\" itemLabel=\"$2\"/>"),
            ("apex:selectOptions\tVisualforce", "apex:selectOptions value=\"$1\"/>"),
            ("apex:selectRadio\tVisualforce", "apex:selectRadio value=\"$1\">\n\t$2\n</apex:selectRadio>"),
            ("apex:stylesheet\tVisualforce", "apex:stylesheet value=\"$1\"/>"),
            ("apex:tab\tVisualforce", "apex:tab label=\"$1\" name=\"$2\"/>"),
            ("apex:tabPanel\tVisualforce", "apex:tabPanel>\n\t$2\n</apex:tabPanel>"),
            ("apex:toolbarGroup\tVisualforce", "apex:toolbarGroup itemSeparator=\"$1\" id=\"$2\">\n\t$3\n</apex:toolbarGroup>"),
            ("apex:variable\tVisualforce", "apex:variable var=\"$1\" value=\"$2\"/>"),
            ("apex:vote\tVisualforce", "apex:vote objectId=\"$1\"/>")
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
